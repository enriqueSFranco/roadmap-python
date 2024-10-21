import asyncio
import logging
from playwright.async_api import async_playwright, Locator, Page, Playwright

logging.basicConfig(
  level=logging.DEBUG, 
  format='%(levelname)s:%(name)s:%(message)s')

logger = logging.getLogger('indeed.py')

URL = 'https://mx.indeed.com/'

class BrowserManager:
  def __init__(self, playwright: Playwright):
    self._browser = None
    self._context = None
    self.playwright = playwright

  async def start(self):
    try:
      logger.info('Iniciando Playwright...')
      chromium = self.playwright.chromium
      self._browser = await chromium.launch(headless=False, slow_mo=1000)
      self._context = await self._browser.new_context()
      logger.info('Navegador y contexto creados.')
    except Exception as exc:
      logger.error(f'Error al iniciar el navegador: {exc}')

  async def close(self):
    if self._context:
      try:
        await self._context.close()
      except Exception as exc:
        logger.error(f'Error al cerrar el contexto: {exc}')
      finally:
        self._context = None
  
    if self._browser:
      try:
        await self._browser.close()
      except Exception as exc:
        logger.error(f'Error al cerrar el navegador: {exc}')
      finally:
        self._browser = None

  async def new_page(self):
    if not self._context:
      raise RuntimeError('El contexto del navegador no está inicializado.')
    return await self._context.new_page()

# Excepcion personalizada
class MissingElementException(Exception):
  def __init__(self, message, code):
    super().__init__(message)
    self.code = code

class ElementVisibilityException(Exception):
  def __init__(self, *args):
    super().__init__(*args)

async def fill_input_field(input: Locator, text: str):
  if await input.count() == 0:
    raise MissingElementException('El elemento no se encontró en el DOM.', code=404)
  if not await input.is_visible():
    raise MissingElementException('El campo no está visible y no se pudo llenar.', code=403)
  try:
    await input.fill(text)
    logger.info(f'El campo ha sido llenado con la información: {text}')
  except Exception as exc:
    logger.error(f'Error al intentar llenar el campo: {exc}')

class IndeedScraper:
  def __init__(self, url):
    self._url = url

  async def fill_input_field(input: Locator, text: str):
    if await input.count() == 0:
      raise MissingElementException('El elemento no se encontró en el DOM.', code=404)
    if not await input.is_visible():
      raise MissingElementException('El campo no está visible y no se pudo llenar.', code=403)
    try:
      await input.fill(text)
      logger.info(f'El campo ha sido llenado con la información: {text}')
    except Exception as exc:
      logger.error(f'Error al intentar llenar el campo: {exc}')

async def main():
  async with async_playwright() as playwright:
    browser_manager = BrowserManager(playwright)
    try:
      await browser_manager.start()
      page = await  browser_manager.new_page()
      
      await page.goto(URL)
      await page.wait_for_selector('form#jobsearch')

      # localizar los inputs dentro del formulario para introducir la informacion
      input_what = page.locator('input#text-input-what')
      input_where = page.locator('input#text-input-where')
      btn_search = page.get_by_text('Buscar empleos')

      if input_what and input_where and btn_search:
        logger.info('✅ Inputs localizados exitosamente')
        # TODO: Manejar los errores para cada input
        await fill_input_field(input_what, 'Desarrollador de software')
        await fill_input_field(input_where, 'Ciudad de México')
        logger.info('✅ Inputs rellenados exitosamente')

        await btn_search.click()
        logger.info('✅ Botón "Buscar empleos" clicado exitosamente')

        # https://mx.indeed.com/jobs?q=react+junior&l=Ciudad+de+M%C3%A9xico&from=searchOnHP&vjk=5cd5ab50cff4e541
        await page.wait_for_url('https://mx.indeed.com/jobs?q=*', timeout=2000)

        # recuperar el elemento que contiene la lista de empleos
        mosaic_jobs_results = page.locator('div[id="mosaic-jobResults"]')
        mosaic_provider_job_cards = mosaic_jobs_results.locator('div[id="mosaic-provider-jobcards"]')
        job_cards = mosaic_provider_job_cards.locator('ul>li')

        titles = []
        for i in range(await job_cards.count()):
          if await job_cards.nth(i).is_visible():
            try:
              job_link = job_cards.nth(i).locator('a')
              await job_cards.nth(i).click()
              if await job_link.get_attribute('aria-pressed'):
                await page.wait_for_load_state('networkidle')
                
                title_element = page.locator('h2.jobsearch-JobInfoHeader-title > span')
                await page.wait_for_selector('h2.jobsearch-JobInfoHeader-title > span')
                title = await title_element.inner_text()
                print(title)
            except Exception as exc:
              logger.error(f'Error: {exc}')
          await asyncio.sleep(1)
      else:
        logger.warning('❌ Inputs no encontrados')

    except Exception as err:
      logger.error(f'Ocurrió un error, {err}')

    finally:
      await browser_manager.close()

if __name__ == '__main__':
  asyncio.run(main())

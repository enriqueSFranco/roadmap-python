import asyncio
import logging
from playwright.async_api import async_playwright, Playwright

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
      logger.info("Iniciando Playwright...")
      chromium = self.playwright.chromium
      self._browser = await chromium.launch(headless=False, slow_mo=1000)
      self._context = await self._browser.new_context()
      logger.info("Navegador y contexto creados.")
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
      raise RuntimeError("El contexto del navegador no está inicializado.")
    return await self._context.new_page()

async def main():
  async with async_playwright() as playwright:
    browser_manager = BrowserManager(playwright)
    try:
      await browser_manager.start()
      page = await  browser_manager.new_page()
      
      await page.goto(URL)
      await page.wait_for_selector('form#jobsearch')

      print(await page.title())
      
      # localizar los inputs dentro del formulario para introducir la informacion
      input_what = page.locator('input#text-input-what')
      input_where = page.locator('input#text-input-where')
      btn_search = page.get_by_text('Buscar empleos')

      if input_what and input_where and btn_search:
        logger.info('✅ Inputs localizados exitosamente')
        await input_what.fill("Desarrollador de software")
        await input_where.fill("Ciudad de México")
        logger.info('✅ Inputs rellenados exitosamente')

        await btn_search.click()
        logger.info('✅ Botón "Buscar empleos" clicado exitosamente')

        # https://mx.indeed.com/jobs?q=react+junior&l=Ciudad+de+M%C3%A9xico&from=searchOnHP&vjk=5cd5ab50cff4e541
        await page.wait_for_url("https://mx.indeed.com/jobs?q=*")
      else:
        logger.warning('❌ Inputs no encontrados')

    except Exception as err:
      logger.error(f'Ocurrió un error, {err}')

    finally:
      await browser_manager.close()

if __name__ == '__main__':
  asyncio.run(main())

# class IndeedScraper:
#   def __init__(self, url):
#     self.url = url
  
#   async def navigate(self, context):
#     pass

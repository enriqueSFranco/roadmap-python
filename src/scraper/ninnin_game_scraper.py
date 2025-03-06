from playwright.async_api import async_playwright, BrowserType, Locator, Page, Playwright
import asyncio
import logging

URL='https://www.nin-nin-game.com/es/'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
QUERY='saint seiya'

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger('Ninningame.py')

class BrowserManager:
  def __init__(self, browser_type: BrowserType):
    self._browser_type = browser_type
    self.browser = None
    self.context = None

  async def setup(self) -> None:
    try:
      logging.info('Iniciando playwright')
      self.browser = await self._browser_type.launch(headless=False, slow_mo=1000)
      self.context = await self.browser.new_context(extra_http_headers=headers)
      logger.info('Context y Navegador creados con exito')
    except Exception as exc:
      logger.error(f'Error al iniciar playwright: {exc}')

  async def close(self) -> None:
    if self.context:
      try:
        logger.info('Contexto cerrado con exito')
        await self.context.close()
      except Exception as exc:
        logger.error(f'No se pudo cerrar el contexto: {exc}')
    
    if self.browser:
      try:
        logger.info('Navegador cerrado con exito')
        await self.browser.close()
      except Exception as exc:
        logger.error(f'No se pudo cerrar el navegador: {exc}')

class NinningameScraper:
  def __init__(self, url):
    self.url = url

async def main():
  async with async_playwright() as playwright: 
    browser = BrowserManager(playwright.chromium)
    try:
      await browser.setup()
      
      page = await browser.context.new_page()
      await page.goto(url=URL)      
      await page.wait_for_load_state('networkidle')

      input_search = page.locator('input[id="search_query_top"]').first
      if input_search:
        logger.info(await input_search.evaluate('node => node.outerHTML'))
        await input_search.click()
        await input_search.fill(QUERY)
        await page.wait_for_url('https://www.nin-nin-game.com/es/search?controller=search&orderby=date_add&orderway=desc&search_query=saint+seiya&submit_search=Buscar')
      else:
        logger.info('No se encontro el input de busqueda')
    except Exception as exc:
      print(f'Error: {exc}')
    finally:
      await browser.close()

if __name__ == '__main__':
  asyncio.run(main())
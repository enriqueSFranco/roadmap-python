import asyncio
import logging

from playwright.async_api import Locator, Page, Playwright, async_playwright

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")

logger = logging.getLogger("indeed.py")

URL = "https://mx.indeed.com/"


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
            logger.error(f"Error al iniciar el navegador: {exc}")

    async def close(self):
        if self._context:
            try:
                await self._context.close()
            except Exception as exc:
                logger.error(f"Error al cerrar el contexto: {exc}")
            finally:
                self._context = None

        if self._browser:
            try:
                await self._browser.close()
            except Exception as exc:
                logger.error(f"Error al cerrar el navegador: {exc}")
            finally:
                self._browser = None

    async def new_page(self):
        if not self._context:
            raise RuntimeError("El contexto del navegador no está inicializado.")
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
        raise MissingElementException("El elemento no se encontró en el DOM.", code=404)
    if not await input.is_visible():
        raise MissingElementException(
            "El campo no está visible y no se pudo llenar.", code=403
        )
    try:
        await input.fill(text)
        logger.info(f"El campo ha sido llenado con la información: {text}")
    except Exception as exc:
        logger.error(f"Error al intentar llenar el campo: {exc}")


class IndeedScraper:
    def __init__(self, url):
        self._url = url

    async def fill_input_field(input: Locator, text: str):
        if await input.count() == 0:
            raise MissingElementException(
                "El elemento no se encontró en el DOM.", code=404
            )
        if not await input.is_visible():
            raise MissingElementException(
                "El campo no está visible y no se pudo llenar.", code=403
            )
        try:
            await input.fill(text)
            logger.info(f"El campo ha sido llenado con la información: {text}")
        except Exception as exc:
            logger.error(f"Error al intentar llenar el campo: {exc}")


async def main():
    async with async_playwright() as playwright:
        browser_manager = BrowserManager(playwright)
        try:
            await browser_manager.start()
            page = await browser_manager.new_page()

            await page.goto(URL)
            await page.wait_for_selector("form#jobsearch")

            # localizar los inputs dentro del formulario para introducir la informacion
            input_what = page.locator("input#text-input-what")
            input_where = page.locator("input#text-input-where")
            btn_search = page.get_by_text("Buscar empleos")

            if input_what and input_where and btn_search:
                logger.info("✅ Inputs localizados exitosamente")
                # TODO: Manejar los errores para cada input
                await fill_input_field(input_what, "Desarrollador de software")
                await fill_input_field(input_where, "Ciudad de México")
                logger.info("✅ Inputs rellenados exitosamente")

                await btn_search.click()
                logger.info('✅ Botón "Buscar empleos" clicado exitosamente')

                # https://mx.indeed.com/jobs?q=react+junior&l=Ciudad+de+M%C3%A9xico&from=searchOnHP&vjk=5cd5ab50cff4e541
                await page.wait_for_url("https://mx.indeed.com/jobs?q=*", timeout=2000)

                # recuperar el elemento que contiene la lista de empleos
                mosaic_jobs_results = page.locator('div[id="mosaic-jobResults"]')
                mosaic_provider_job_cards = mosaic_jobs_results.locator(
                    'div[id="mosaic-provider-jobcards"]'
                )
                job_cards = mosaic_provider_job_cards.locator("ul>li")

                titles = []
                for i in range(await job_cards.count()):
                    if await job_cards.nth(i).is_visible():
                        try:
                            job_link = job_cards.nth(i).locator("a")
                            await job_cards.nth(i).click()
                            if await job_link.get_attribute("aria-pressed"):
                                await page.wait_for_load_state("networkidle")

                                title_element = page.locator(
                                    "h2.jobsearch-JobInfoHeader-title > span"
                                )
                                await page.wait_for_selector(
                                    "h2.jobsearch-JobInfoHeader-title > span"
                                )
                                title = await title_element.inner_text()
                                print(title)
                        except Exception as exc:
                            logger.error(f"Error: {exc}")
                    await asyncio.sleep(1)
            else:
                logger.warning("❌ Inputs no encontrados")

        except Exception as err:
            logger.error(f"Ocurrió un error, {err}")

        finally:
            await browser_manager.close()


if __name__ == "__main__":
    asyncio.run(main())

"""
  1.- Informacion de la vacante
  -Titulo
  -Sueldo
  -Requerimientos
  -Ubicacion
  -Fecha de publicacion
  -Experiencia
  -Idioma

  2.- Limpieza de datos
  -Eliminar datos duplicados
  -Normalizacion de los datos

  3.- Exploracion de los datos (Exploratory Data Analysis o EDA)
  -Distribución de Vacantes por Título: ¿Cuáles son los roles más comunes? ¿Hay más vacantes para desarrollador web, desarrollador JS, etc.? Puedes usar visualizaciones de barras o pie charts.
  
  -Distribución Geográfica: Si has recopilado información sobre la ubicación de las vacantes, podrías analizar en qué ciudades o regiones hay más demanda de ciertos perfiles. Usar mapas es una buena opción.
  
  -Salarios Promedio por Rol o Ubicación: Si tienes datos de salario, es interesante analizar los rangos salariales. ¿El salario promedio varía mucho dependiendo de la ubicación o el rol?
  
  -Tiempo de Publicación: Analiza cómo el tiempo de publicación influye en la cantidad de vacantes disponibles. Por ejemplo, si las vacantes más antiguas tienen menos ofertas de trabajo, esto podría darte una idea de la demanda de ciertos perfiles.

  4.- Analisis mas avanzado
  -Correlación entre Requisitos y Salario: ¿Los puestos con más requisitos (por ejemplo, experiencia, educación, habilidades específicas) ofrecen salarios más altos?
  
  -Clusterización de Vacantes: Podrías aplicar técnicas de clustering (como k-means) para agrupar las vacantes similares en términos de título, habilidades requeridas, salario y ubicación. Esto puede ayudarte a identificar patrones o "niches" dentro del mercado laboral.
  
  -Análisis de Sentimiento de las Descripciones de Trabajo: Si tienes acceso a las descripciones completas de las vacantes, podrías hacer un análisis de sentimiento (¿es un trabajo con un enfoque positivo, motivador? ¿Es estresante o negativo?) usando técnicas de procesamiento de lenguaje natural (NLP).
  
  -Modelos Predictivos: Podrías desarrollar un modelo que prediga el salario en función de las características de la vacante, como título, ubicación, y experiencia requerida. Esto te permitirá demostrar habilidades de modelado y predicción.

  4. Plantear un Problema
En cuanto al enfoque del problema, aquí tienes algunas ideas sobre cómo podrías abordarlo desde una perspectiva de Data Science:

a) Predicción de Salario:
Plantea el siguiente problema: "¿Cuáles son los factores que mejor predicen el salario para una vacante de desarrollador?" Podrías crear un modelo predictivo para estimar el salario en función de características como:

Título de la vacante.
Ubicación.
Experiencia requerida.
Requisitos técnicos (por ejemplo, conocimientos en React, JS, etc.).
b) Análisis de Tendencias de Empleo:
"¿Cómo han cambiado las demandas de habilidades y tecnologías en el tiempo?" Si tienes datos históricos (por ejemplo, por fecha de publicación), podrías hacer un análisis de tendencias para identificar qué tecnologías o lenguajes de programación están siendo más demandados.

c) Segmentación del Mercado de Trabajo:
"¿Cuáles son los nichos más relevantes dentro del mercado de trabajo para desarrolladores?" Aquí podrías aplicar clustering o segmentación para agrupar vacantes similares y determinar qué combinaciones de habilidades y requisitos se repiten con mayor frecuencia.

d) Análisis Geográfico:
"¿Cómo varía la demanda de desarrolladores web entre diferentes regiones o ciudades?" Esto podría involucrar una visualización geográfica o análisis de correlaciones entre el salario y la ubicación.

5. Visualización de Resultados
Una vez que hayas realizado el análisis, es muy importante presentar los resultados de manera clara y atractiva. Utiliza gráficas y visualizaciones como:

Gráficas de barras, pie charts y diagramas de dispersión.
Mapas de calor para la distribución geográfica.
Gráficas de línea para mostrar la evolución de tendencias a lo largo del tiempo.
Puedes usar herramientas como matplotlib, seaborn, plotly (para gráficos interactivos), o incluso Tableau si prefieres trabajar en una plataforma de BI.

6. Conclusiones y Recomendaciones
En la última parte de tu análisis, deberías generar conclusiones basadas en los resultados obtenidos y tal vez dar recomendaciones. Por ejemplo:

¿Qué habilidades están más relacionadas con salarios altos?
¿En qué ciudades hay una mayor demanda de desarrolladores web?
¿Qué tecnologías están en auge?
7. Herramientas y Recursos
Si necesitas herramientas para hacer el análisis y modelado, aquí te dejo algunas sugerencias:

Python (con librerías como pandas, numpy, scikit-learn, seaborn, matplotlib).
Jupyter Notebooks para realizar todo el análisis de forma interactiva.
SQL (si decides almacenar los datos en una base de datos).
Power BI o Tableau para visualización interactiva.
"""

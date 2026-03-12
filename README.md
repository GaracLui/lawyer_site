![Estado del Proyecto](https://img.shields.io/badge/Estado-En_Desarrollo-yellow) 
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) 
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white) 
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white) 
![Docker](https://img.shields.io/badge/Docker-fds?style=flat-square&logo=docker&logoColor=white&labelColor=%232496ED&color=%232496ED) 
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat&logo=tailwind-css&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat&logo=vite&logoColor=white)
![UV](https://img.shields.io/badge/UV-000000?style=flat&logo=uv&logoColor=white)


# ⚖️ Sistema de gestión de la práctica jurídica (remake)

**🚀 The Evolution: From Legacy PHP to Modern Django**

Este proyecto es una reestructuración completa del sitio web de un bufete de abogados profesional. Migré una arquitectura antigua de **CodeIgniter 4/Bootstrap 5** a un ecosistema de **Django/Tailwind**.

## 🛠️ **Tecnológica utilizada y arquitectura**

- **Backend:** Django 6.+.+ (Python) con una estructura modular de "Apps".
- **Base de datos:** PostgreSQL para una gestión robusta de datos relacionales.
- **Frontend:** Tailwind CSS para una estética legal de alta gama y con un diseño boutique.
- **Alojamiento de imágenes:** Cloudinary (CDN) para garantizar una entrega global ultrarrápida.
- **Seguridad:** Protección CSRF de Django y encabezados SSL seguros.

## ✨ **Características principales**

- **CMS dinámico:** Un panel de administración de Django personalizado donde el abogado puede editar cada texto, actualizar áreas de servicio y cambiar la ubicación de la oficina sin necesidad de modificar el código.
- **Motor SEO:** Generación automatizada de slugs y metaetiquetas OpenGraph para una alta visibilidad en Google y vistas previas en redes sociales.
- **Gestión de clientes potenciales:** Formulario de contacto integrado que guarda las consultas en PostgreSQL y envía alertas por correo electrónico al abogado en tiempo real.
- **Diseño adaptable:** Diseño boutique "Mobile-first" que utiliza los sistemas de cuadrícula y tipografía de Tailwind.

## 📂 **Estructura del proyecto**

```
.
├── .venv/                    # Entorno virtual para dependencias de Python (no incluido)
├── about/                    # App de Django para la sección "Sobre Nosotros"
├── blog/                     # App de Django para la sección "Blog"
├── contact/                  # App de Django para la sección "Contacto"
├── core/                     # App de Django para funcionalidades comunes 
├── media/                    # Archivos subidos por el cliente (imágenes, documentos)
├── services/                 # App de Django para la sección "Servicios"
├── assets/                   # Front-end source files
│   ├── javascript/           #             
│   └── styles/               # 
├── static/                   # Built front-end assets (generated)
│   ├── css/
│   └── js/
├── templates/                # Django templates
│   ├── about/
│   ├── blog/
│   ├── contact/
│   ├── core/
│   │   ├── base.html         # Plantilla base con bloques para heredar
│   │   ├── footer.html       # Pie de página común a todas las páginas
│   │   └── navbar.html       # Barra de navegación común a todas las páginas
│   └── services/
├── lawyer_site/              # Django project settings
│   ├── settings.py
│   └── urls.py
├── .env                      # Archivo de variables de entorno (no incluido)
├── Dockerfile
├── docker-compose.yaml
├── manage.py
├── package.json              # Node.js dependencies
├── pyproject.toml            # Python dependencies
├── uv.lock                   # Lockfile para dependencias de Python
└── vite.config.js            # Vite configuration
```

## ⚙️ **Instalación y configuración**

1. **Clona el repositorio:**
   ```
   # Instala dependencias de Python
   uv sync
   # o con pip (si no usas UV):
   # pip install .
   ```

2. **Installar dependencias JavaScript:**
   ```
   npm install
   ```

3. **Variables de entorno:**
   *Crea un archivo `.env` donde agregaras tus credenciales.*
   ```
   POSTGRES_DB=dev_database
   POSTGRES_USER=catanist
   POSTGRES_PASSWORD=catan_champion
   DB_HOST=db
   DB_PORT=5432

   SECRET_KEY='|your_catan_website_super_password|'
   DEBUG=True
   ```

4. **Crea (o reconstruye) las imágenes para todos los servicios definidos en su archivo `docker-compose.yaml` y luego crea, inicia y adjunta los contenedores para esos servicios:**
   ```
   docker compose up --build
   ```

5. **Realiza una migración basada en los modelos de Django (estando activo Docker):**
   ```
   docker exec [container_name] uv manage.py makemigrations
   ```

6. **Aplica las migraciones:**
   ```
   docker exec [container_name] uv manage.py migrate
   ```

7. **Crea un `superuser` dentro de la carpeta `[container_name]`:**
   ```
   docker compose exec [web] uv manage.py createsuperuser
   ```

8. **Ejecutar en modo desarrollo:**
   ```
   npm run dev
   ```
   ```
   docker compose exec [web] uv manage.py runserver
   ```


## 📦 **Packages y apps instalado/a/s**

Es posible que no he logrado integrar al projecto ciertos packages y apps ó al querer ejecutar el sitio web se necesiten posteriores acciones.

- [x] `uv` para la gestión de entornos virtuales y dependencias.
- [x] `Django` para el desarrollo del backend.
- [x] `psycopg[binary]` para la conexión con PostgreSQL.
- [x] `pillow` para la manipulación de imágenes.
- [x] `node.js` y `npm` para compilar Tailwind CSS y Vite.
- [x] `vite` para la gestión de assets frontend.
- [x] `django-vite` para integrar Vite con Django.
- [x] `tailwindcss` para el diseño frontend.
- [x] `django-unfold` para admin personalizado.
- [ ] `docker` para contenerizar la aplicación.
- [ ] `cloudinary` para la gestión de imágenes en la nube.

## 🎯 **Motivación**

Observé que el sitio anterior dependía de id de base de datos especificos y CSS manual. Implementé un Singleton Pattern para la configuración y utilicé Cloudinary para la optimización de imágenes con el fin de mejorar el LCP (Largest Contentful Paint).

Este proyecto demuestra la capacidad de refactorizar código heredado en sistemas modernos y fáciles de mantener. Se centra en la experiencia de usuario (UX) para el administrador del sitio y en el rendimiento para el usuario final.

## ⚠️ Disclaimer

Este es un proyecto con fines educativos y de demostración. Las imágenes de productos (libros, juegos, personajes) utilizadas en la base de datos de prueba pertenecen a sus respectivos autores y marcas registradas. No existe intención comercial real ni lucro con la propiedad intelectual de terceros.

## ✒️ Autor

   Garacciolo Luis Alfredo

   www.linkedin.com/in/garacciolo-luis-alfredo

Hecho con ❤️ y Python.
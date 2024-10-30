# OnlyFlans

OnlyFlans es una aplicación web desarrollada en Django que permite a los usuarios explorar una variedad de flanes, acceder a información exclusiva y realizar acciones de autenticación en un entorno seguro. El proyecto incorpora funciones avanzadas de manejo de usuarios, contenido personalizado y control de acceso a vistas protegidas.

## Características

- **Exploración de Flanes:** Muestra una galería de flanes en la página principal. Los flanes pueden ser públicos o privados, y se muestran de acuerdo a las configuraciones de privacidad.
- **Autenticación de Usuarios:** Sistema de autenticación que permite a los usuarios registrarse, iniciar sesión y cerrar sesión.
- **Vistas Protegidas:** El contenido privado solo es visible para usuarios autenticados. Utilizamos el decorador `login_required` para proteger el acceso a la página de bienvenida.
- **Redirección Personalizada:** Los usuarios autenticados son redirigidos automáticamente a la página de bienvenida, mientras que al cerrar sesión son redirigidos a la página de despedida.
- **Interfaz Personalizada:** Diseño responsivo con Bootstrap y uso de tarjetas para la visualización de flanes. Barra de navegación dinámica que muestra diferentes opciones según el estado de autenticación del usuario.

## Estructura del Proyecto

- **Modelos:** La aplicación cuenta con un modelo principal `Flan`, que define las propiedades básicas de cada flan, como su nombre, descripción y configuración de privacidad (`is_private`).
- **Vistas y Rutas:**
  - `/`: Página de inicio donde se muestran flanes públicos.
  - `/bienvenido`: Página de bienvenida para usuarios autenticados donde se muestran los flanes privados.
  - `/acerca`: Página estática con información sobre el sitio.
  - **Páginas de Autenticación:** Login y logout con redirecciones configuradas en `settings.py` (`LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL`).
- **Templates:** 
  - **index.html:** Muestra los flanes públicos.
  - **welcome.html:** Muestra los flanes privados para usuarios autenticados.
  - **goodbye.html:** Página de despedida que aparece después de cerrar sesión.
  - **acerca.html:** Página estática con información sobre el proyecto.


### Autor
- [Rosa Rubio](https://github.com/PaulinaRubioP)

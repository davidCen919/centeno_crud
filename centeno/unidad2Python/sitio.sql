-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-12-2023 a las 15:15:45
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sitio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulos`
--

CREATE TABLE `articulos` (
  `id_articulo` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `articulos`
--

INSERT INTO `articulos` (`id_articulo`, `nombre`, `descripcion`, `url`) VALUES
(1, 'Procesador I-Core I7', 'Para el buen rendimiento', 'https://imgs.search.brave.com/38W_l7zUG-_ctzj7CfF-ydyuAjvnD2WBTfo5E9EsetM/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMtbmEuc3NsLWlt/YWdlcy1hbWF6b24u/Y29tL2ltYWdlcy9J/LzUxQXFFa2MyQnVM/LmpwZw'),
(2, 'Antivirus McAfee', ' Total Protection ', 'https://www.officedepot.com.mx/medias/81341-1200ftw?context=bWFzdGVyfHJvb3R8MTg0MDM0fGltYWdlL2pwZWd8aDdmL2hkOC85NDg1Mzc0ODQ5MDU0LmpwZ3xlOGM2YmUxMTZjOTdmNGM0ZjkwMzliMzk1ZmY1ZGIxM2ZmMmZjZTBjOTNkZDA5OTQzNTU1YmQ0YmIzNjY0MWQ5'),
(3, 'Arduino', 'open-source', 'https://logowik.com/content/uploads/images/arduino5804.jpg'),
(4, 'visual studio code', 'editor de código', 'https://blog.cloudanalogy.com/wp-content/uploads/2020/03/vsc-01.jpg'),
(5, 'Windows ', '11', 'https://cuscoinformatico.com/storage/windows-11-home.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `juegos`
--

CREATE TABLE `juegos` (
  `id_juego` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `juegos`
--

INSERT INTO `juegos` (`id_juego`, `nombre`, `descripcion`, `url`) VALUES
(2, 'GTV 4', 'Juego Buenoo', 'https://imgs.search.brave.com/OdUJ_ElT_qwzxNgT21Hu4NXgXjiRpKQLbRX8XH2lQxs/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJjYXZlLmNv/bS93cC9CUkNqTnJX/LmpwZw'),
(4, 'Prince of Persia: ', 'The Lost Crown', 'https://image.api.playstation.com/vulcan/ap/rnd/202305/2309/02a7644b160e11678ca5332d6e0eb5fdd87902aa3087d446.png'),
(5, 'Jujutsu Kaisen: ', 'Cursed Clash', 'https://m.media-amazon.com/images/I/81Hh9dWL3NL._AC_UF1000,1000_QL80_.jpg'),
(6, 'Spider-Man ', '2', 'https://image.api.playstation.com/vulcan/ap/rnd/202306/1301/cabf0ac92702b06e7f3140c6e64f05269ceca449e61d1498.png'),
(7, 'Metroid Prime ', 'Remastered', 'https://m.media-amazon.com/images/I/71B+DjKegPL._AC_UF1000,1000_QL80_.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `imagen` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`id`, `nombre`, `imagen`, `url`) VALUES
(2, 'ANGELA', 'GALVAN.png', 'https://imgs.search.brave.com/gJ3uGZpVXjDdRdfNTb0R42B6mdSZZgE7K21tRLepI58/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/ZWNhcnRlbGVyYS5j/b20vY2FydGVsZXMv/NTEwMC81MTUxLzAw/MV9wLmpwZw'),
(3, 'GUADALUPE', 'ALANIS.png', 'https://imgs.search.brave.com/xV2Ecg172rZ3rsWDWBqZ-Y2rZM_fCeFUKXPoKKIeADY/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/Y3VlbnRvc2RlcHJp/bmNlc2FzLmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvMjAxOS8x/Mi9sYS1wcmluY2Vz/YS15LWVsLXNhcG8u/anBn'),
(4, 'SANTIAGO ', 'POOL.PNG', 'https://imgs.search.brave.com/qwCZX-pDoxWZw_N-I7qA72kS4GjzJp7tLP07Quafm9U/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9jZG4u/Y3VsdHVyYWdlbmlh/bC5jb20vZXMvaW1h/Z2VuZXMvdW4tbXVu/ZG8tZmVsaXotY2tl/LmpwZw'),
(5, 'TIAGO', 'MEEE.PNG', 'https://imgs.search.brave.com/WxdeN8aKZY0Lm4JQoinEnRjE_VhfqcXQ9EFS0LeZzcw/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9jZG4u/Y3VsdHVyYWdlbmlh/bC5jb20vZXMvaW1h/Z2VuZXMvZWwtbGli/cm8tbmVncm8tZGUt/bGFzLWhvcmFzLWNr/ZS5qcGc'),
(6, 'JUAN', 'SS.png', 'https://imgs.search.brave.com/FV8k3c_EJEbm7-BGS-gNUINVcsbTssaqQjaSrYLLguk/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXNzbDUuY2FzYWRl/bGxpYnJvLmNvbS9h/L2wvczUvMzUvOTc4/ODQxOTQyMTEzNS53/ZWJw');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `peliculas`
--

CREATE TABLE `peliculas` (
  `id_pelicula` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `peliculas`
--

INSERT INTO `peliculas` (`id_pelicula`, `nombre`, `descripcion`, `url`) VALUES
(5, 'SAW X', 'Pelicula de terror', 'https://imgs.search.brave.com/UuTvmGbMt25IvVH_BPJdijLex_IEbnk8_UcNSdij0_8/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/ZGVhcGxhbmV0YS5j/b20vdXBsb2Fkcy8y/MDIzMDgwMS9TYXdY/X1Bvc3Rlcl8yMzAu/anBn'),
(10, 'Deadpool ', '3', 'https://i.pinimg.com/736x/a1/1b/0e/a11b0e6f27a1816bfef6009ec44454fd.jpg'),
(11, 'Kraven ', 'the Hunter', 'https://m.media-amazon.com/images/M/MV5BZWNhOWY4OTUtNDIwZC00ZTMzLTgzNDgtZGU5OWM0ODcwYmVlXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_.jpg'),
(12, 'Beetlejuice ', '2', 'https://www.elimparcial.com/__export/1679967243777/sites/elimparcial/img/2023/03/27/336887900_136624655789534_7067160973046569569_n.jpg_1369687503.jpg'),
(13, 'Kung Fu Panda ', '4', 'https://pbs.twimg.com/media/FZ_0gVGWQAIQo8G.jpg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `articulos`
--
ALTER TABLE `articulos`
  ADD PRIMARY KEY (`id_articulo`);

--
-- Indices de la tabla `juegos`
--
ALTER TABLE `juegos`
  ADD PRIMARY KEY (`id_juego`);

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `peliculas`
--
ALTER TABLE `peliculas`
  ADD PRIMARY KEY (`id_pelicula`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `articulos`
--
ALTER TABLE `articulos`
  MODIFY `id_articulo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `juegos`
--
ALTER TABLE `juegos`
  MODIFY `id_juego` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `libros`
--
ALTER TABLE `libros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `peliculas`
--
ALTER TABLE `peliculas`
  MODIFY `id_pelicula` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

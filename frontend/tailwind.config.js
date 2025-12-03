/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**/*.html",
        "./src/**/*.js",
        "./node_modules/flowbite/**/*.js"
    ],
    safelist: [
        {
            pattern: /(bg|text)-(blue|indigo)-(50|100|600|700|800)/,
            variants: ['hover', 'focus'],
        }
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('flowbite/plugin')
    ],
}

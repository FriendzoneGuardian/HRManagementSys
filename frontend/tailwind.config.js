/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**/*.html",
        "./src/**/*.js",
        "./node_modules/flowbite/**/*.js"
    ],
    safelist: [
        {
            pattern: /(bg|text|border|ring)-(blue|indigo|violet|teal)-(50|100|200|300|600|700|800)/,
            variants: ['hover', 'focus', 'group-hover'],
        }
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('flowbite/plugin')
    ],
}

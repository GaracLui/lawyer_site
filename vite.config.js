import { defineConfig } from 'vite';
import path from 'path';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
    plugins: [tailwindcss()],
    base: '/static/', // This should match the STATIC_URL in your Django settings.py
    build: {
        // Ehere Vite will output the built files
        // This should match the STATIC_ROOT in your Django settings.py
        outDir: path.resolve(__dirname, './static'),
        emptyOutDir: false,             // Don't delete existing files in the output directory
        manifest: "manifest.json",      // Generate a manifest file for Django to read
        rollupOptions: {
            input: {
                style: path.resolve(__dirname, './assets/styles/style.css'),
                main: path.resolve(__dirname, './assets/javascript/main.js')
            },
            output: {
                // Output JS bundle with a name that includes the entry point name
                entryFileNames: `js/[name]-bundle.js`,
                assetFileNames: `css/[name].css`,
            },
        },
    },
});
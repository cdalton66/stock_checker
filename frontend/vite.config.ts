import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    port: 3000,
    host: '0.0.0.0',
    proxy: {
      '/api': {
        target: process.env.VITE_API_URL || 'http://localhost:5001',
        changeOrigin: true
      }
    }
  },
  build: {
    outDir: 'dist',
    sourcemap: true
  }
})

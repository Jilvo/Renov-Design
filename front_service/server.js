// Utilisez import au lieu de require
import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const app = express();

// Convertir __dirname en ES module (puisqu'il n'existe pas directement)
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Servir les fichiers statiques depuis dist
app.use(express.static(path.join(__dirname, 'dist')));

// Rediriger toutes les routes vers index.html
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

// Lancer le serveur
const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

const path = require('path');

module.exports = {
  entry: './static/js/main.js', // Ensure this points to your main JS file
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  mode: 'production', // Or 'development'
};

const express = require('express');
const fetch = require('node-fetch');
const app = express();
app.use(express.json());
const MODEL = process.env.MODEL_URL || 'http://model_server:8001';
const OPT = process.env.OPT_URL || 'http://optimizer:8002';
app.post('/predict/soh', async (req, res) => {
  const r = await fetch(MODEL + '/predict/soh', {method:'POST', body: JSON.stringify(req.body), headers:{'Content-Type':'application/json'}});
  const j = await r.json();
  res.json(j);
});
app.post('/optimize/charging', async (req,res)=> {
  const r = await fetch(OPT + '/optimize/charging', {method:'POST', body: JSON.stringify(req.body), headers:{'Content-Type':'application/json'}});
  res.json(await r.json());
});
app.listen(8003, ()=>console.log('API gateway on 8003'));

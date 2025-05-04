const express = require('express') ;

const app = express() ;
const port = 4200 ;
app.get('/',(req,res)=>{
('./nav.html', {root: __dirname})
    res.sendFile('./public/home.html', {root: __dirname}) ;
}) ;
 app.get('/view',(req,res)=>{
     res.sendFile('./public/view.html', {root: __dirname}) ;
 }) ;
app.get('/create',(req,res)=>{
res.sendFile('./public/create.html', {root: __dirname}) ;
}) ;
app.listen(port, (req,res)=>{
    console.log(`listening on port ${port}`);
})
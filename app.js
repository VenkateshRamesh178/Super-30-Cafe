const express=require("express");
const bodyParser=require("body-parser");
// const request =require("request");
// const https=require("https");

const app=express();
app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended:true}));
app.set('view engine', 'ejs');

app.get("/",function(req,res){
  res.render("homepage");

});

app.get("/:menu",function (req,res) {
  res.render("menu");

});
app.listen(5000,function(){
  console.log("server is up and running on port 5000");
})

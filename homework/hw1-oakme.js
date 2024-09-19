import { Application } from "https://deno.land/x/oak/mod.ts";

const app = new Application();

app.use((ctx) => {
  //ctx.response.status = 404
  console.log('url=', ctx.request.url)
//   ctx.response.body = 'Not Found!'

  let pathname = ctx.request.url.pathname
  if (pathname == '/'){ctx.response.body = `<html>
    <body>
    <h1>我的自我介紹</h1>
    <ol>
    <li><a href="/name">姓名</a></li>
    <li><a href="/age">年齡</a></li>
    <li><a href="/gender">性別</a></li>
    <li><a href="/github">github</a></li>
  
    
    </ol>
    </body>
    </html>
    `
    
  }
  else if (pathname == '/name') {
    ctx.response.body = '王莉允'
  } 
  else if (pathname == '/age') {
    ctx.response.body = '21'
  } 
  else if (pathname == '/gender') {
    ctx.response.body = '女'
  } 

  else if (pathname == '/github') {
    ctx.response.redirect('https://github.com/LainGH0601?tab=repositories')
  }
  else {
    ctx.response.body = 'Not Found!'
  }
  
});

console.log('start at : http://127.0.0.1:8000')
await app.listen({ port: 8000 })
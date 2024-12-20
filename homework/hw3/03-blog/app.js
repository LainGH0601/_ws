import { Application, Router } from "https://deno.land/x/oak/mod.ts";
import * as render from './render.js'
import { DB } from "https://deno.land/x/sqlite/mod.ts";

const db = new DB("blog.db");
db.query("CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT , body TEXT ,user TEXT )");
db.query("INSERT INTO posts (title,user, body) VALUES (?,?, ?)", ['11','22', '33']);
const router = new Router();

router.get('/', userList) // 根據不同用戶顯示貼文列表
  .get('/:user/', list)
  .get('/:user/post/new', add)
  .get('/:user/post/:id', show)
  .post('/:user/post', create);

const app = new Application();
app.use(router.routes());
app.use(router.allowedMethods());

// 顯示某個用戶的貼文列表
async function userList(ctx) {
  const users = db.query("SELECT DISTINCT user FROM posts"); // 獲取唯一用戶
  console.log('22',users)
  ctx.response.body = await render.userList(users);
}


function query(sql) {
  let list = []
  for (const [id, title, body, user] of db.query(sql)) {
    list.push({id, title, body, user})
  }
  return list
}

async function list(ctx) {
  // const user = ctx.params.user;
 
  let list = []
  for (const [id, title, body, user] of db.query(`SELECT id, title, body, user FROM posts WHERE user = ?`, [ctx.params.user])) {
    list.push({id, title, body, user});
  }
  console.log(list);
  ctx.response.body = await render.list(list);
}

async function add(ctx) {
  ctx.response.body = await render.newPost();
}

async function show(ctx) {
  const pid = ctx.params.id;
  const user = ctx.params.user;
  //const posts = query(`SELECT id, title, body, user FROM posts WHERE id = ? AND user = ?`, [pid, user]);
  let list = []
  for (const [id, title, body, user] of db.query(`SELECT id, title, body, user FROM posts WHERE id = ? AND user = ?`, [pid,ctx.params.user])) {
    list.push({id, title, body, user});
  }
  const post = list.length ? list[0] : null;

  if (!post) ctx.throw(404, 'Post not found');
  ctx.response.body = await render.show(post);
}



async function create(ctx) {
  const body = ctx.request.body
  if (body.type() === "form") {
    const pairs = await body.form()
    const post = {}
    for (const [key, value] of pairs) {
      post[key] = value
    }
    console.log('create:post=', post)
    db.query("INSERT INTO posts (title,user, body) VALUES (?,?, ?)", [post.title,post.user, post.body]);
    ctx.response.redirect('/');
  }
}

let port = parseInt(Deno.args[0])
// console.log(`Server run at http://127.0.0.1:${port}`)
// await app.listen({ port });

console.log('Server run at http://127.0.0.1:8000')
await app.listen({ port: 8000 });

export function layout(user="1",title, content) {
  return `
  <html>
  <head>
    <title>${user}:${title}</title>
    <style>
      body {
        padding: 80px;
        font: 16px Helvetica, Arial;
      }
  
      h1 {
        font-size: 2em;
      }
  
      h2 {
        font-size: 1.2em;
      }
  
      #posts {
        margin: 0;
        padding: 0;
      }
  
      #posts li {
        margin: 40px 0;
        padding: 0;
        padding-bottom: 20px;
        border-bottom: 1px solid #eee;
        list-style: none;
      }
  
      #posts li:last-child {
        border-bottom: none;
      }
  
      textarea {
        width: 500px;
        height: 300px;
      }
  
      input[type=text],
      textarea {
        border: 1px solid #eee;
        border-top-color: #ddd;
        border-left-color: #ddd;
        border-radius: 2px;
        padding: 15px;
        font-size: .8em;
      }
  
      input[type=text] {
        width: 500px;
      }
    </style>
  </head>
  <body>
    <section id="content">
      ${content}
    </section>
  </body>
  </html>
  `
}

// 顯示某個用戶的貼文列表
export function userList(users) {
    let listHtml = []
    for (let user of users) {
        listHtml.push(`<li><a href="/${user}/">${user}</a></li>`)
    }
    return layout('', 'User List', `<ol>${listHtml.join('\n')}</ol>`)
}

export function list(posts) {
  let list = posts.map(post => `
    <li>
      <h1>${post.user}</h1>
      <h2>${post.title}</h2>
      <p><a href="/${post.user}/post/${post.id}">Read post</a></p>
    </li>
  `);
  let content = `
    <h1>Posts</h1>
    <p>You have <strong>${posts.length}</strong> posts!</p>
    <p><a href="/${posts[0]?.user}/post/new">Create a Post</a></p>
    <ul id="posts">
      ${list.join('\n')}
    </ul>
  `;
  return layout('', 'Posts', content);
}


export function newPost(user) {
  return layout(user, 'New Post', `
    <h1>New Post</h1>
    <p>Create a new post.</p>
    <form action="/${user}/post" method="post">
      <p><input type="text" placeholder="Title" name="title"></p>
      <p><input type="text" placeholder="user" name="user"></p>
      <p><textarea placeholder="Contents" name="body"></textarea></p>
      <p><input type="submit" value="Create"></p>
    </form>
  `);
}


export function show(post) {
  return layout(post.user,post.title, `
    <h1>${post.title}</h1>
    <p>${post.body}</p>
  `)
}

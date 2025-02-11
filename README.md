# Personal Web Page

Hi, this repository contains the code for my personal web page, built using **Jekyll**, a static site generator widely used for personal websites and blogs. Jekyll is supported by GitHub Pages, making it an excellent choice for hosting a simple yet customizable website.

I am a beginner at web development, but I have learned a lot during the three days I spent building this site.

![Myself](assets/images/20240416_153409.jpg)

## File Structure

I am using the `minima` Jekyll theme. One interesting feature of Jekyll themes is that you don't need to include the full file structure in your project, as the necessary files are already present within the installed `minima` theme. To access those files, you can run the following command in the terminal:

```sh
bundle info --path minima
```

If you want to modify something, you can copy the relevant files into your project and make changes as needed.

### `_layouts` and `_includes`

- The `_layouts` folder contains **HTML templates** that define the structure of different pages (e.g., the homepage, individual posts).
- The `_includes` folder contains **reusable components** like the footer, header, or sidebar.

These templates determine where and how the content of the pages is presented.

The most important file in `_layouts` is `default.html`, which acts as a base template. It loads common elements like stylesheets and scripts that should appear on all pages. For example, I added links to my custom **CSS file** and **Font Awesome icons** inside `default.html`.

### Root Files

The actual page content is stored in files located at the root of the directory, such as `sobre-mi.markdown` and `blog.html`. These files contain Markdown content combined with the layout instructions from `_layouts` to generate complete web pages.

For example:
- `index.markdown` contains the content for the homepage.
- This file is processed first through `default.html` (common layout) and then through `home.html` (specific layout for the homepage).
- The connection between content and layout is established through YAML front matter in each file.

### `_posts`

Blog posts are stored inside the `_posts` folder. Each post is written in Markdown and follows a specific filename format:

```sh
YYYY-MM-DD-title-of-post.markdown
```

Jekyll processes these files using `_layouts/post.html`, ensuring that all posts follow a consistent structure. This means you can modify `post.html` to change the appearance of all blog posts at once.

### `assets`

The `assets` folder contains media files such as **images, audio, videos, and documents**. Files are organized by type (`images`, `videos`, `docs`, etc.) and can be accessed through relative paths.

I try to keep file sizes low because I noticed that large files (e.g., videos over 300 KB) can cause rendering issues.

#### CSS Styling

My custom **CSS file** is also stored in the `assets` folder. I included it in `default.html` to style different parts of the website, such as the blog sidebar and post thumbnails. By defining CSS classes, I can apply consistent styling across multiple pages.

### `scripts`

While working on the project, I wrote **Python scripts** to automate certain tasks. These scripts are stored in the `scripts` folder but do not interact with the website's building process. I keep them for future use in case I need to repeat those tasks.

### `_site`

The `_site` folder is **automatically generated** by Jekyll and should not be manually modified. It contains the final HTML, CSS, and JavaScript files that are displayed on the live website.

Any direct changes made in `_site` will be **overwritten** the next time Jekyll builds the site.

## Additional Notes

I find Jekyll’s templating system quite powerful. Some features I’ve explored include:

- Using **global variables** to insert common elements (e.g., my ORCID ID in the footer).
- Structuring posts efficiently with **YAML front matter**.
- Understanding how themes work and customizing them when necessary.

I am still learning a lot about Jekyll and web development. There are files and configurations I have not yet explored, and I am continuously improving my understanding of how different parts of the system work.

This README reflects the knowledge I gained during my first three days working on this project. Feedback and suggestions are always welcome!


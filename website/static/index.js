function deleteBlog(blogId) {
    fetch('/delete-blog', {
        method: 'POST',
        body: JSON.stringify({ blogId: blogId })
    }).then((response) => {
        window.location.href = "/";
    });
}
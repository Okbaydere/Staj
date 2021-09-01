function deleteNote(task_id) {
  fetch("/<int:task_id>", {
    method: "DELETE",
    body: JSON.stringify({ task_id: task_id }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

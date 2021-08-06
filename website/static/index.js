function deleteNote(noteId) {
	fetch('/delete-note',{
		method:'POST',
		body: JSON.stringify({nodeId: noteId})
	}).then((_res) => {
		window.location.href="/";
	})
}
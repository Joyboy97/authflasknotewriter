function deleteNote(noteId){
    fetch("/delete-note",{
        method:"POST",
        body: JSON.stringify({noteId: noteId})
        //makes a JSON out of the form method POST data 
    }).then((_res)=>{
        window.location.href="/";
        // puts you back at the home page
    });
}

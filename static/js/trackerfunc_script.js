function copySpiel()
{
    var copybtn  = document.querySelector('#copybutton');
    copybtn.textContent = 'Spiel Copied!';
    copybtn.disabled = true;
    const mySmartTextarea = document.createElement('textarea');
    mySmartTextarea.innerHTML = document.getElementById("finalspiel").innerText;
    const parentElement = document.body.appendChild(mySmartTextarea);
    mySmartTextarea.select();
    document.execCommand('copy');
    parentElement.removeChild(mySmartTextarea);
}

function showDraft(evt, draftId, commentId) {
            
    var i, drafts, buttons, comments;

    drafts = document.getElementsByClassName("draftbox");
    for (i = 0; i < drafts.length; i++) {
    drafts[i].style.display = "none";
    }

    comments = document.getElementsByClassName("commentbox");
    for (i = 0; i < comments.length; i++) {
    comments[i].style.display = "none";
    }

    buttons = document.getElementsByClassName("tabbutton");
    for (i = 0; i < buttons.length; i++) {
    buttons[i].className = buttons[i].className.replace(" tabactive", "");
    }

    
    document.getElementById(draftId).style.display = "flex";
    if(commentId!=null)
    {
    document.getElementById(commentId).style.display = "block";
    
    }
    evt.currentTarget.className += " tabactive";

    if (draftId != "newdraftbox")
    {
        document.getElementById("uploadButton").classList.remove("tabactive");
    }
}
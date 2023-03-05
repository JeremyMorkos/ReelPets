// validate profile page form when logged in.
const validateForm = (event) => {
    const name = document.forms["register"]["name"].value;
    const type = document.forms["register"]["type"].value;
    const imageUrl = document.forms["register"]["image_url"].value;
    const favouriteFood = document.forms["register"]["favourite_food"].value;
    if (name === "" || type === "" || imageUrl === "" || favouriteFood === "")  {
        alert("All fields must be filled out");
        event.preventDefault(); 
        return false;
    }
    return true;
}

const profileBtn = document.querySelector('#profile_btn')
if (profileBtn)
    profileBtn.addEventListener('click', validateForm) 


const buttons = document.querySelectorAll('.heart_button')

//Create a fetch for the heart button, when the heart is clicked do not refresh the page
for (let i = 0 ; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function(event) {
        const button = event.target;
        
        fetch(`/hearts?pet_id=${button.dataset.petId}`, {
            method: 'POST'
        })
    })
}

    
            
  

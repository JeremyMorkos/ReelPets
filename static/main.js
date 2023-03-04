// validate profile page form when logged in.
const validateForm = (event) => {
    const name = document.forms["register"]["name"].value;
    const type = document.forms["register"]["type"].value;
    const imageUrl = document.forms["register"]["image_url"].value;
    const favouriteFood = document.forms["register"]["favourite_food"].value;
    if (name === "" || type === "" || imageUrl === "" || favouriteFood === "")  {
        alert("All fields must be filled out");
        event.preventDefault() 
        return false;
    }
    return true;
  }
 
  const profileBtn = document.querySelector('#profile_btn')
  profileBtn.addEventListener('click', validateForm) 



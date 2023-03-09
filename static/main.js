
const validateProfile = (event) => {
    const name = document.forms["register"]["name"].value;
    const type = document.forms["register"]["type"].value;
    const imageUrl = document.forms["register"]["image"].value;
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
    profileBtn.addEventListener('click', validateProfile) 


const validateSignup = (event) => {
    const user_name = document.forms["signup"]["user_name"].value;
    const imageUrl = document.forms["signup"]["image"].value;
    const password = document.forms["signup"]["password"].value;
    const password_check = document.forms["signup"]["password_check"].value;
 
 
    if (user_name === "" || imageUrl ==="" || password === "" || password_check === "")  {
        alert("All fields must be filled out");
        event.preventDefault(); 
        return false;
    }
    return true;
}

const signupBtn = document.querySelector('#signup')
if (signupBtn)
    signupBtn.addEventListener('click', validateSignup)



const buttons = document.querySelectorAll('.heart_button')
 
for (let i = 0 ; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function(event) {
        const button = event.target;


        // fetch - performs http request ( get/post) - then fill the request. - returns a Promise
        fetch(`/hearts?pet_id=${button.dataset.petId}`, {
            method: 'POST'
        })
        // .then waits for the promise to resolve, and then executes a function
        .then(async (response) => {
            console.log(response);
            const json = await response.json();
            console.log(json);

            return json;
        }) 
        .then((data) => {
            
            numHearts = document.querySelector(`#num_hearts_${button.dataset.petId}`)
            numHearts.innerText = data.num_hearts
        
        })
 
    })
}

    
            
  

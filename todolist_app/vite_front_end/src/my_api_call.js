import Cookies from "js-cookie";

export default function loadObjects() {
    let my_token = Cookies.get('my_access_token');
    let full_token = "Bearer " + my_token

    fetch("http://127.0.0.1:8000/todos/", {
        method:'GET',
        headers: {"Authorization": full_token}, 
        //body: JSON.stringify({"email": "asd@email.com", "password": "string"})
    })
    .then(response => console.log(response))
    .catch(error => console.error(error));
}

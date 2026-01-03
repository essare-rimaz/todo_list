
export default async function login() {
  // Collect form data
  const email = document.getElementById('exampleInputEmail1').value;
  const password = document.getElementById('exampleInputPassword1').value;

  var formData = new FormData();
  formData.append("username", email);
  formData.append("password", password);


    // Make the API call
    const res = await fetch("http://127.0.0.1:8000/token/", {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: formData
    });

    const result = await res.json();
    console.log(result)

    //console.log(response)
    //document.cookie = `access_token=${jwtToken}; Secure; HttpOnly; SameSite=Strict; Path=/; Max-Age=3600`;

}
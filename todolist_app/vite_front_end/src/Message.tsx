// PascalCasing -> expected in React

// in React whatever looks like HTML is actually converted into javascript
// try putting <h1> hello world </h1> with setting React runtime to classic in https://babeljs.io/repl
function Message() {
    const name = 'Terezka';
    if (name)
        return <h1>Hello {name}</h1>;
    return <h1>Hello world</h1>
}

export default Message
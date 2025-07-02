import { Fragment } from "react/jsx-runtime";
import { useState } from "react";

function ListGroup() {
    let items = [
        'asd',
        'asdfg',
        'qwre',
        'asdgf'
    ];
    
    //hook
    const [selectedIndex, setSelectedIndex] = useState(-1);


    //items = []

    if (items.length === 0)
        return (
        <>
            <h1>List</h1>
            <p>No item found</p>
        </>
        );
    return (
        // component can render only one element, 
        // if you want more you need to use something like fragment or empty <></>
        <Fragment>
            <h1>List of things</h1>
            { items.length === 0 && <p>No item found</p>}
            <ul className="list-group">
                {items.map((item, index) => (
                    <li 
                        className={ selectedIndex===index ? "list-group-item active" : "list-group-item"}
                        key={item} 
                        onClick={() => { setSelectedIndex(index); }}
                    >
                        {item}
                    </li>
                ))}
            </ul>
        </Fragment>
    )
}
export default ListGroup;
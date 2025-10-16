import { Fragment } from "react/jsx-runtime";
import { useState } from "react";

// components shouldnt contain much business logic, because then they are not reusable

// properties are arguments of a function
interface ListGroupProps {
    items: string[];
    heading: string;
    onSelectItem: (item: string) => void; // the type of this parameter is a function which takes string and returns void
}

function ListGroup({ items, heading, onSelectItem}: ListGroupProps) {

    
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
            <h1>{heading}</h1>
            { items.length === 0 && <p>No item found</p>}
            <ul className="list-group">
                {items.map((item, index) => (
                    <li 
                        className={ selectedIndex===index ? "list-group-item active" : "list-group-item"}
                        key={item} 
                        onClick={() => { setSelectedIndex(index); 
                        onSelectItem(item)
                        }}
                    >
                        {item}
                    </li>
                ))}
            </ul>
        </Fragment>
    )
}
export default ListGroup;
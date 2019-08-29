import React from "react"

import "./Block.css"

function Block(props) {
    console.log(props.src)
    return (
        <div id='block'>
          <img
            src={props.src}
            alt='testing'
          />
        </div>
    )
}

export default Block

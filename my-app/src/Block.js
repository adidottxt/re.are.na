import React from "react"

import "./Block.css"

function Block(props) {
    return (
        <div id='block'>
          <a href={props.src}>
            <img
              src={props.src}
              alt='testing'
            />
          </a>
        </div>
    )
}

export default Block

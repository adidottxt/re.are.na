import React from "react"

import "../css/Block.css"

function Block(props) {
    return (
        <div id='media-block'>
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

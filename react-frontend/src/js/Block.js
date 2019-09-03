import React from "react"

import "../css/Block.css"

function Block(props) {
    return (
        <div id='media-block'>
          <a href={props.linksrc}>
            <img
              src={props.imgsrc}
              alt='block'
            />
          </a>
        </div>
    )
}

export default Block

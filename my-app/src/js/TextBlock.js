import React from "react"

import "../css/TextBlock.css"

function TextBlock(props) {
    return (
        <div id='block'>
          <a href={props.linksrc}>
            <div className='text-data'>{props.text}</div>
          </a>
        </div>
    )
}

export default TextBlock

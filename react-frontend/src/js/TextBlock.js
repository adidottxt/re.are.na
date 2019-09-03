import React from "react"

import "../css/TextBlock.css"

function TextBlock(props) {
    return (
        <a href={props.linksrc} target="_blank" rel="noopener noreferrer">
          <div id='block'>
              <div className='text-data'>{props.text}</div>
          </div>
        </a>
    )
}

export default TextBlock

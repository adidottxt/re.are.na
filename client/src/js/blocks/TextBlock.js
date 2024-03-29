import React from "react"

import "../../css/TextBlock.css"

function TextBlock(props) {
  return (
    <div id='block'>
      <a href={props.linksrc} target="_blank" rel="noopener noreferrer">
        <div id='text-data'>{props.text}</div>
      </a>
    </div>
  )
}

export default TextBlock

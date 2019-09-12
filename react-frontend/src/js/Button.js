import React from "react"

import '../css/Button.css'

function Button(props) {
    return (
      <div id='button-div'>
        <button id='button' onClick={() => console.log("clicked")}>{props.text}</button>
      </div>
    )
}

export default Button

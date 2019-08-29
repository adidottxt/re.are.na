import React from "react"
import '../css/Button.css'

function Button(props) {
    return (
      <button id='button'>{props.text}</button>
    )
}

export default Button

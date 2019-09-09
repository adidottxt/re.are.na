import React from "react"

import TextBlock from "./TextBlock"
import BlockInfo from "./BlockInfo"

import "../css/Row.css"

function TextRow(props) {
    return (
      <div id='row'>
        <TextBlock linksrc={props.linksrc} text={props.text} />
        <BlockInfo
            title={props.title}
            channel={props.channel}
            date={props.date}
        />
      </div>
    )
}

export default TextRow

import React from "react"

import TextBlock from "../blocks/TextBlock"
import BlockInfo from "../blocks/BlockInfo"

import "../../css/Row.css"

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

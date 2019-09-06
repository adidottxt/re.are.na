import React from "react"

import TextBlock from "./TextBlock"
import BlockInfo from "./BlockInfo"

function TextRow(props) {
    return (
      <>
        <TextBlock linksrc={props.linksrc} text={props.text} />
        <BlockInfo
            title={props.title}
            channel={props.channel}
            date={props.date}
        />
      </>
    )
}

export default TextRow

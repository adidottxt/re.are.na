import React from "react"

import EmptyBlock from "./EmptyBlock"
import BlockInfo from "./BlockInfo"

import "../css/Row.css"

function EmptyRow(props) {
    return (
      <div id='row'>
        <EmptyBlock />
        <BlockInfo
            title=''
            channel=''
            date=''
        />
      </div>
    )
}

export default EmptyRow

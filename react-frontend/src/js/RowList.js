import React, { Component } from "react"
import { gql } from 'apollo-boost'
import { graphql } from 'react-apollo'

import Row from "./Row"
import TextRow from "./TextRow"

import "../css/RowList.css"

const getBlocksDataQuery = gql`
{
  allBlocks {
      edges {
          node {
            blockContent
            blockId
            blockUrl
            blockType
            blockTitle
            blockCreateDate
            channelTitle
            requestId
          }
      }
  }
}
`

class RowList extends Component {

  displayBlocks() {
      var data = this.props.data;
      if (data.loading) {
          return (
            <div id='loading-screen'>
              <img src='../static/loading.gif' alt='loading' id='loading'/>
            </div>
          )
      } else {
          var i;
          var highestRequest = 0;
          var requestId = 0;
          for (i = 0; i < data.allBlocks.edges.length; i++) {
              requestId = Number(data.allBlocks.edges[i].node.requestId)
              if (requestId > highestRequest) {
                  highestRequest = requestId;
              }
          }
          return data.allBlocks.edges.map(block => {
              requestId = block.node.requestId
              if (requestId !== 1 && requestId > highestRequest-3) {
                if (block.node.blockType === 'Text') {
                    return <TextRow
                        linksrc={block.node.blockUrl}
                        text={block.node.blockContent}
                        title={block.node.blockTitle}
                        channel={block.node.channelTitle}
                        date={block.node.blockCreateDate}
                    />
                } else if (block.node.blockUrl !== 'test') {
                    return <Row
                      imgsrc={block.node.blockContent}
                      linksrc={block.node.blockUrl}
                      title={block.node.blockTitle}
                      channel={block.node.channelTitle}
                      date={block.node.blockCreateDate}
                    />
                }
              } return '';
          })
      }
  }

  render() {
    return (
        <div>
            {this.displayBlocks()}
        </div>
    )
  }
}

export default graphql(getBlocksDataQuery)(RowList)

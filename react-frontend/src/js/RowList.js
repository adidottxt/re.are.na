import React, { Component } from "react"
import { gql } from 'apollo-boost'
import { graphql } from 'react-apollo'

import Row from "./Row"
import TextRow from "./TextRow"

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
          }
      }
  }
}
`

class RowList extends Component {
  displayBlocks() {
      console.log(this.props.data)
      var data = this.props.data;
      if (data.loading) {
          return(<div>Loading blocks...</div>)
      } else {
          return data.allBlocks.edges.map(block => {
              if (block.node.blockType === 'Text') {
                  console.log(block.node.blockType)
                  return <TextRow
                      linksrc={block.node.blockUrl}
                      text={block.node.blockContent}
                      title={block.node.blockTitle}
                      channel={block.node.channelTitle}
                      date={block.node.blockCreateDate}
                  />
              } else if (block.node.blockUrl !== 'test') {
                    console.log(block.node.blockType)
                    return <Row
                      imgsrc={block.node.blockContent}
                      linksrc={block.node.blockUrl}
                      title={block.node.blockTitle}
                      channel={block.node.channelTitle}
                      date={block.node.blockCreateDate}
                    />
              } else {
                  return '';
              }
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

import React from "react"
import { gql } from 'apollo-boost'
// import { graphql } from 'react-apollo'
import{ useQuery } from '@apollo/react-hooks'

import MediaRow from "./MediaRow"
import EmptyRow from "./EmptyRow"
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
            requestId
          }
      }
  }
}
`

function RowList() {
    const { loading, error, data } = useQuery(getBlocksDataQuery);
    if (loading) {
        return (
            <>
                <EmptyRow />
                <EmptyRow />
                <EmptyRow />
            </>
        )
    }

    if (error) return "Error! $(error.message)";

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
                return <MediaRow
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

export default RowList

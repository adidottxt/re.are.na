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
            imageUrl
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

// function RowList(props) {
class RowList extends Component {
  render() {
    console.log(this.props)
    return (
        <div>
            <Row
                imgsrc='https://d2w9rnfcy7mm78.cloudfront.net/4771939/original_1c3af1831f95e7d71d0674227c114072.jpg?1565150930'
                linksrc='https://are.na/block/123123'
                title='test-title'
                channel='test-chan'
                date='test-date'
            />

            <Row
                imgsrc='https://d2w9rnfcy7mm78.cloudfront.net/4633641/display_94c1620f3ef1f7d2dc7008d0849f39b8.png?1563197545'
                title='test-title'
                linksrc='https://are.na/block/123124'
                channel='test-chan'
                date='test-date'
            />

            <TextRow
                linksrc='https://are.na/block/4184924'
                text='testingtttttttttttttttttttttttttttttttttttttttttestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttestingestingestingestingestingestingestingestingestingestingestingestingesttttttttttttttttttttttttttttttttttttttttttestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingesting'
                title=''
                channel='snippets'
                date='test-date'
            />

        </div>
    )
  }
}

export default graphql(getBlocksDataQuery)(RowList)

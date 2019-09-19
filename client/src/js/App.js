import React from "react"
import ApolloClient from 'apollo-boost'
import { ApolloProvider } from 'react-apollo'

import Header from "./header/Header"
import HeaderInfo from "./header/HeaderInfo"
import Content from "./content/Content"
import ContentContextProvider from "./content/ContentContext"

import "../css/App.css"

// Apollo Client setup
const client = new ApolloClient({
  uri: 'http://localhost:5000/graphql'
})


function App() {
  return (
    <ApolloProvider client={client}>
      <>
        <Header />
        <HeaderInfo />
        <ContentContextProvider>
          <Content />
        </ContentContextProvider>
      </>
    </ApolloProvider>
  )
}

export default App

import React from "react";
import { graphql, useStaticQuery } from "gatsby";
import { About } from "./About";

const ABOUT_QUERY = graphql`
  query AboutQuery {
    allMarkdownRemark(
      filter: { frontmatter: { templateKey: { eq: "about" } } }
    ) {
      edges {
        node {
          id
          frontmatter {
            templateKey
            headerText
            subText
            aboutSection
            aboutImage {
              publicURL
              childImageSharp {
                fluid {
                  ...GatsbyImageSharpFluid_withWebp_noBase64
                }
              }
            }
          }
        }
      }
    }
  }
`;

export const AboutContainer = ({ content }) => {
  return <About content={content} />;
};

export default () => {
  const data = useStaticQuery(ABOUT_QUERY);
  return <AboutContainer content={data} />;
};

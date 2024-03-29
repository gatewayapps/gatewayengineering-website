import styled from "styled-components";

const MainContentOuterDiv = styled.div`
  display: flex;
  justify-content: center;
  background-color: #545454;
  margin-bottom: -100px;
  flex-direction: column;
  align-items: center;
`;
const MainContentInnerTopDiv = styled.div`
  max-width: 90%;
  width: 1200px;
  justify-self: center;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: #fff;
  transform: translate(0px, -100px);
  border-radius: 8px;
`;
const MainContentTextWrapper = styled.div`
  max-width: 80%;
  text-align: center;
  margin: 50px 0;
`;
const MainContentHeaderText = styled.h2`
  margin: 20px 0;
  font-size: 28px;
  line-height: 1.3;
`;
const MainContentSubText = styled.p`
  margin: 80px 0;
`;
const ImageDiv = styled.div`
  width: 100%;
  > img {
    width: 100%;
  }
`;
const MainContentInnerBottomDiv = styled.div`
  margin-top: 50px;
  max-width: 90%;
  width: 1200px;
  justify-self: center;
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
  background-color: #fff;
  transform: translate(0px, -100px);
  padding: 40px 0 20px;
  border-radius: 8px 8px 0 0;
`;
const Service = styled.div`
  max-width: 40%;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 10px;
  box-shadow: 10px 10px 35px -20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  transition: box-shadow 0.2s ease, transform 0.2s ease;
  > a {
    text-decoration: none;
    color: #000;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  &:hover {
    transform: translate(-2px, -2px);
    box-shadow: 15px 25px 40px -25px;
    transition: box-shadow 0.2s ease, transform 0.2s ease;
  }
  @media (max-width: 1000px) {
    max-width: 80%;
  }
`;
const ServiceTitle = styled.h3`
  font-size: 32px;
`;
const ServiceDescription = styled.p`
  font-size: 18px;
  @media (max-width: 500px) {
    font-size: 16px;
  }
`;
const ServiceImageDiv = styled.div`
  width: 80%;
  > img {
    width: 100%;
  }
`;

export {
  MainContentOuterDiv,
  MainContentInnerTopDiv,
  MainContentInnerBottomDiv,
  MainContentTextWrapper,
  MainContentHeaderText,
  MainContentSubText,
  ImageDiv,
  Service,
  ServiceTitle,
  ServiceDescription,
  ServiceImageDiv
};

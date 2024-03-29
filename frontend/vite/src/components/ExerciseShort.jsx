import { Card, Image, Text, Box } from "grommet";
import { FormNext } from "grommet-icons";
import Dumbbell from "../assets/dumbbell.png";
export default function ExerciseShort(props) {
  return (
    <Card
      direction="row"
      fill="horizontal"
      gap="none"
      pad="small"
      hoverIndicator={true}
      style={{ boxShadow: "rgba(0, 0, 0, 0.68) 0px 2px 4px" }}
    >
      <FormNext style={{ flex: 1 }} />
      <Text style={{ flex: 10 }}>{props.title}</Text>
      <Text textAlign="end" style={{ flex: 2 }}>
        {props.sets}x{props.reps}
      </Text>
    </Card>
  );
}

import { useEffect } from "react";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
  CardFooter,
} from "../components/ui/card";
import { Label } from "../components/ui/label";
import { Input } from "../components/ui/input";
import { Button, buttonVariants } from "../components/ui/button";
import { Message } from "../components/ui/Message";
import { Textarea } from "../components/ui/textarea";
import { useForm } from "react-hook-form";
import { useTask } from "../context/TasksContext";
import { useNavigate, useParams, Link } from "react-router-dom";
function TaskFormEdit() {
  const { tasks, createTask, getTask, updateTask } = useTask();
  const navigate = useNavigate();

  const { register, handleSubmit, setValue } = useForm();
  const params = useParams();

  const onSubmit = handleSubmit((values) => {
    try {
      if (params.id) updateTask(params.id, values);

      navigate("/tasks");
    } catch (error) {
      console.log(error);
    }
  });
  useEffect(() => {
    async function loadTask() {
      if (params.id) {
        const task = await getTask(params.id);
        console.log(task);
        setValue("title", task.title);
        setValue("description", task.description);
      }
    }
    loadTask();
  }, []);
  return (
    <div className="h-screen flex justify-center items-center">
      <Card className="bg-zinc-800 text-white">
        <CardHeader>
          <CardTitle className="flex justify-between">
            Edit Tasks
            <Link className={buttonVariants()} to="/tasks">
              Go back
            </Link>
          </CardTitle>
        </CardHeader>

        <CardContent>
          <form onSubmit={onSubmit}>
            <Label>Tile</Label>
            <Input
              type="text"
              {...register("title", { required: true })}
              autoFocus
              className="bg-zinc-700"
            />

            <Label>Description</Label>
            <Textarea
              rows="3"
              placeholder="Enter description"
              {...register("description", { required: true })}
              className="bg-zinc-700 text-white"
            ></Textarea>

            <Button type="submit" className="my-2 bg-zinc-700">
              Edit Task
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}

export default TaskFormEdit;
def demo1(runner_class_name, implementation_class_name):

    print('Dynamically create and execute ' + runner_class_name + ' in ' + implementation_class_name)

    # dynamically import and create base classes for runner and implementation
    runner_class = getattr(__import__('runnerlib'), runner_class_name)
    implementation_class = getattr(__import__('implementationlib'), implementation_class_name)

    # dynamically create the full class from both runner and implementation
    full_class_name = runner_class_name + '_' + implementation_class_name
    action1version1 = type(full_class_name, (implementation_class, runner_class), {})

    # instantiate the dynamic full class and run it as demonstration
    a1v1 = action1version1()
    print(type(a1v1))
    a1v1.run()


def demo2(runners, implementations):

    print('Dynamically create and execute all action+implementation pairs.')

    for runner_name in runners:
        for implementation_name in implementations:
            demo1(runner_name, implementation_name)


def main():

    runners = ['RunnerAction1', 'RunnerAction2']
    implementations = ['ImplementationVersion1', 'ImplementationVersion2']

    demo2(runners, implementations)


if __name__ == "__main__":
    main()
